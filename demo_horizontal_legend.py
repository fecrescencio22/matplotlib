#!/usr/bin/env python
"""
Demo script showing expected behavior of horizontal_legend feature.
This creates comparison plots to visualize row-wise vs column-wise filling.

NOTE: This uses the standard legend() with reordered items to simulate
      what horizontal_legend() will do once your changes are built/installed.
"""

import matplotlib.pyplot as plt
import numpy as np

def demo_basic_comparison():
    """Compare standard legend vs simulated horizontal legend."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    fig.suptitle('Horizontal Legend Feature - Row-wise vs Column-wise Filling',
                 fontsize=14, fontweight='bold')

    # Create 6 sample lines
    colors = ['red', 'blue', 'green', 'orange', 'purple', 'brown']

    # Left plot: Standard legend (column-wise)
    for i, color in enumerate(colors):
        ax1.plot([0, 1, 2], [i, i+0.5, i], color=color, linewidth=2, label=f'Item {i}')

    ax1.set_title('Standard Legend (ncols=3)\nColumn-wise: 0, 2, 4 | 1, 3, 5',
                  fontsize=12)
    ax1.legend(ncols=3, loc='upper center', bbox_to_anchor=(0.5, -0.05))
    ax1.set_xlabel('X axis')
    ax1.set_ylabel('Y axis')
    ax1.grid(True, alpha=0.3)

    # Right plot: Simulated horizontal legend (row-wise)
    lines = []
    for i, color in enumerate(colors):
        line, = ax2.plot([0, 1, 2], [i, i+0.5, i], color=color, linewidth=2)
        lines.append(line)

    ax2.set_title('Horizontal Legend (max_per_row=3)\nRow-wise: 0, 1, 2 | 3, 4, 5',
                  fontsize=12)

    # Simulate horizontal legend by reordering handles
    # Standard legend with ncols=3 fills: [0,2,4], [1,3,5] (column-wise)
    # We want: [0,1,2], [3,4,5] (row-wise)
    # So we reorder to: [0,3,1,4,2,5] which will fill column-wise as our row-wise layout
    reordered_handles = [lines[0], lines[3], lines[1], lines[4], lines[2], lines[5]]
    reordered_labels = ['Item 0', 'Item 3', 'Item 1', 'Item 4', 'Item 2', 'Item 5']

    ax2.legend(reordered_handles, reordered_labels, ncols=3,
               loc='upper center', bbox_to_anchor=(0.5, -0.05))
    ax2.set_xlabel('X axis')
    ax2.set_ylabel('Y axis')
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    return fig


def demo_many_items():
    """Demo with many items showing wrapping behavior."""
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))
    fig.suptitle('Horizontal Legend - Wrapping with Many Items',
                 fontsize=14, fontweight='bold')

    n_items = 10

    # Top plot: 5 per row
    for i in range(n_items):
        ax1.plot([i, i+1], [i, i+1], linewidth=2, label=f'Dataset {i}')

    ax1.set_title('max_per_row=5 (simulated)\n2 rows: [0,1,2,3,4] | [5,6,7,8,9]',
                  fontsize=12)
    ax1.legend(ncols=5, loc='upper center', bbox_to_anchor=(0.5, -0.05))
    ax1.grid(True, alpha=0.3)

    # Bottom plot: 3 per row
    for i in range(n_items):
        ax2.plot([i, i+1], [i, i+1], linewidth=2, label=f'Dataset {i}')

    ax2.set_title('max_per_row=3 (simulated)\n4 rows: [0,1,2] | [3,4,5] | [6,7,8] | [9]',
                  fontsize=12)
    ax2.legend(ncols=3, loc='upper center', bbox_to_anchor=(0.5, -0.05))
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    return fig


def demo_use_cases():
    """Show typical use cases for horizontal legends."""
    fig = plt.figure(figsize=(14, 10))
    fig.suptitle('Horizontal Legend Use Cases', fontsize=14, fontweight='bold')

    # Use case 1: Time series with many series
    ax1 = plt.subplot(2, 2, 1)
    time = np.linspace(0, 10, 100)
    for i in range(6):
        ax1.plot(time, np.sin(time + i*0.5), label=f'Sensor {i+1}')
    ax1.set_title('Time Series Data\n(6 sensors, 3 per row)')
    ax1.legend(ncols=3, loc='upper center', bbox_to_anchor=(0.5, -0.05),
               frameon=True, shadow=True)
    ax1.set_xlabel('Time (s)')
    ax1.set_ylabel('Value')
    ax1.grid(True, alpha=0.3)

    # Use case 2: Comparison plot
    ax2 = plt.subplot(2, 2, 2)
    categories = ['Q1', 'Q2', 'Q3', 'Q4']
    for i, year in enumerate([2021, 2022, 2023, 2024]):
        values = np.random.randint(50, 100, 4)
        ax2.plot(categories, values, 'o-', linewidth=2, markersize=8, label=f'{year}')
    ax2.set_title('Quarterly Comparison\n(4 years, all in one row)')
    ax2.legend(ncols=4, loc='upper center', bbox_to_anchor=(0.5, -0.05),
               frameon=True)
    ax2.set_ylabel('Revenue ($M)')
    ax2.grid(True, alpha=0.3)

    # Use case 3: Scientific plot with parameters
    ax3 = plt.subplot(2, 2, 3)
    x = np.linspace(0, 5, 100)
    params = [0.5, 1.0, 1.5, 2.0, 2.5, 3.0]
    for param in params:
        ax3.plot(x, np.exp(-x/param), label=f'λ={param}')
    ax3.set_title('Exponential Decay\n(6 parameters, 3 per row)')
    ax3.legend(ncols=3, loc='upper right', frameon=True)
    ax3.set_xlabel('x')
    ax3.set_ylabel('f(x)')
    ax3.grid(True, alpha=0.3)

    # Use case 4: Multiple categories
    ax4 = plt.subplot(2, 2, 4)
    x = np.arange(5)
    categories = ['Region A', 'Region B', 'Region C', 'Region D', 'Region E']
    width = 0.15
    for i, category in enumerate(categories):
        offset = width * (i - 2)
        ax4.bar(x + offset, np.random.randint(20, 80, 5), width, label=category)
    ax4.set_title('Regional Data\n(5 regions, all in one row)')
    ax4.legend(ncols=5, loc='upper center', bbox_to_anchor=(0.5, -0.08),
               frameon=True)
    ax4.set_xlabel('Category')
    ax4.set_ylabel('Value')
    ax4.set_xticks(x)
    ax4.set_xticklabels(['Cat 1', 'Cat 2', 'Cat 3', 'Cat 4', 'Cat 5'])
    ax4.grid(True, alpha=0.3, axis='y')

    plt.tight_layout()
    return fig


def main():
    """Run all demos."""
    print("="*70)
    print("HORIZONTAL LEGEND FEATURE - EXPECTED BEHAVIOR DEMO")
    print("="*70)
    print("\nThis demo shows what your horizontal_legend feature will do")
    print("once your changes are built and installed.")
    print("\nGenerating demo figures...")

    # Create demos
    fig1 = demo_basic_comparison()
    fig1.savefig('demo_1_basic_comparison.png', dpi=150, bbox_inches='tight')
    print("  [OK] Saved: demo_1_basic_comparison.png")

    fig2 = demo_many_items()
    fig2.savefig('demo_2_many_items.png', dpi=150, bbox_inches='tight')
    print("  [OK] Saved: demo_2_many_items.png")

    fig3 = demo_use_cases()
    fig3.savefig('demo_3_use_cases.png', dpi=150, bbox_inches='tight')
    print("  [OK] Saved: demo_3_use_cases.png")

    print("\n" + "="*70)
    print("Demo figures created successfully!")
    print("="*70)
    print("\nThe horizontal_legend() method will:")
    print("  • Arrange items in ROWS (horizontally first)")
    print("  • Wrap to new rows after 'max_per_row' items")
    print("  • Work with ax.horizontal_legend(), fig.horizontal_legend(),")
    print("    and plt.horizontal_legend()")
    print("\nCurrent standard legend() arranges items in COLUMNS (vertically first)")
    print("\nClose the windows to exit...")

    plt.show()


if __name__ == '__main__':
    main()
