"""
Visualizes FastText sentence embedding clusters using Scikit-Learn TSNE and Matplotlib.
Usage:
    python helper_scripts/tsne_visualizer.py
"""

import os
import json
import numpy as np
from sklearn.cluster import KMeans
from sklearn.manifold import TSNE

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(SCRIPT_DIR, "embedded_data_short.json")


def visualize():
    if not os.path.exists(DATA_FILE):
        print(f"Error: Embedded data file not found at {DATA_FILE}")
        return

    with open(DATA_FILE, "r", encoding="utf-8") as file:
        data = json.load(file)

    X = []
    labels = []
    for intent in data.get('intents', []):
        tag = intent.get('tag', '')
        if tag != 'general':
            for pattern in intent.get('patterns', []):
                X.append(pattern)
                labels.append(tag)

    if not X:
        print("Error: No embedding patterns found in data file.")
        return

    X = np.array(X)
    print(f"Loaded {len(X)} embedding vectors of dimension {X.shape[1]}.")

    # Cluster embeddings using KMeans
    clusters = KMeans(n_clusters=5, n_init='auto', random_state=42)
    cluster_labels = clusters.fit_predict(X)

    # Dimensionality reduction via Scikit-Learn t-SNE
    print("Computing 2D t-SNE projection...")
    tsne = TSNE(n_components=2, random_state=42, perplexity=30, max_iter=1000)
    X_embedded = tsne.fit_transform(X)

    # Plot using matplotlib
    try:
        import matplotlib.pyplot as plt

        plt.figure(figsize=(10, 7))
        scatter = plt.scatter(
            X_embedded[:, 0],
            X_embedded[:, 1],
            c=cluster_labels,
            cmap='tab10',
            alpha=0.75,
            edgecolors='k',
            linewidths=0.5
        )
        plt.colorbar(scatter, label='Cluster')
        plt.title("t-SNE Clustering of Intent FastText Embeddings", fontsize=14)
        plt.xlabel("t-SNE Dimension 1", fontsize=11)
        plt.ylabel("t-SNE Dimension 2", fontsize=11)
        plt.grid(True, linestyle='--', alpha=0.5)

        output_image = os.path.join(SCRIPT_DIR, "tsne_clusters.png")
        plt.savefig(output_image, dpi=150, bbox_inches='tight')
        print(f"Visualization saved to: {output_image}")

        # Display window if GUI display is available
        try:
            plt.show()
        except Exception:
            pass

    except ImportError:
        print("\nMatplotlib is not installed.")
        print("To generate cluster plots, install matplotlib:")
        print("    pip install matplotlib\n")


if __name__ == '__main__':
    visualize()