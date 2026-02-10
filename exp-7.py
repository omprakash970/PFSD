import os
import argparse
import matplotlib.pyplot as plt


def generate_line_chart(output_dir: str):
    """Generate a simple line chart and save as PNG."""
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
    values = [12, 18, 7, 22, 15, 25]

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(months, values, marker="o", linewidth=2, color="#1f77b4")
    ax.set_title("Basic Line Chart")
    ax.set_xlabel("Month")
    ax.set_ylabel("Value")
    ax.grid(True, linestyle="--", alpha=0.5)

    out_path = os.path.join(output_dir, "line_chart.png")
    fig.savefig(out_path, dpi=150, bbox_inches="tight")
    return fig, out_path


def generate_pie_chart(output_dir: str):
    """Generate a simple pie chart and save as PNG."""
    labels = ["Apples", "Bananas", "Cherries", "Dates"]
    sizes = [30, 25, 20, 25]

    fig, ax = plt.subplots(figsize=(6, 6))
    wedges, texts, autotexts = ax.pie(
        sizes,
        labels=labels,
        autopct="%1.0f%%",
        startangle=90,
        colors=["#ff9999", "#66b3ff", "#99ff99", "#ffcc99"],
    )
    ax.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.
    ax.set_title("Basic Pie Chart")

    out_path = os.path.join(output_dir, "pie_chart.png")
    fig.savefig(out_path, dpi=150, bbox_inches="tight")
    return fig, out_path


def main():
    parser = argparse.ArgumentParser(description="Generate a basic line and pie chart using matplotlib.")
    parser.add_argument(
        "--output-dir",
        default=".",
        help="Directory to save generated images (default: current directory)",
    )
    parser.add_argument(
        "--show",
        action="store_true",
        help="Display charts in a window after generating.",
    )
    parser.add_argument(
        "--no-show",
        action="store_true",
        help="Do not display charts (overrides --show).",
    )
    args = parser.parse_args()

    output_dir = os.path.abspath(args.output_dir)
    os.makedirs(output_dir, exist_ok=True)

    figs = []
    fig1, path1 = generate_line_chart(output_dir)
    figs.append(fig1)
    print(f"Saved line chart to: {path1}")

    fig2, path2 = generate_pie_chart(output_dir)
    figs.append(fig2)
    print(f"Saved pie chart to: {path2}")

    if args.show and not args.no_show:
        plt.show()
    else:
        # Close figures to free memory in non-show mode
        for f in figs:
            plt.close(f)


if __name__ == "__main__":
    main()
