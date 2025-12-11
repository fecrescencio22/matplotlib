#!/usr/bin/env python
"""
Simple manual test script for horizontal_legend feature.
This adds the local matplotlib lib to the path to use your changes.
"""

import sys
import os

# Add local matplotlib to path
lib_path = os.path.join(os.path.dirname(__file__), 'lib')
if lib_path not in sys.path:
    sys.path.insert(0, lib_path)

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.legend as mlegend

print(f"Using matplotlib from: {plt.__file__}")

def test_basic():
    """Test 1: Basic functionality"""
    print("\nTest 1: Basic horizontal_legend creation...")
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3], label="Line 1")
    ax.plot([2, 3, 4], label="Line 2")
    ax.plot([3, 4, 5], label="Line 3")

    try:
        leg = ax.horizontal_legend()
        print(f"  - Created: {type(leg).__name__}")
        print(f"  - Number of items: {len(leg.get_texts())}")
        print(f"  - max_per_row: {leg._max_per_row}")

        assert isinstance(leg, mlegend.HorizontalLegend), "Should create HorizontalLegend instance"
        assert len(leg.get_texts()) == 3, "Should have 3 legend entries"
        assert leg._max_per_row == 4, "Default max_per_row should be 4"
        print("  [PASSED]")
    except Exception as e:
        print(f"  [FAILED]: {e}")
        import traceback
        traceback.print_exc()
    finally:
        plt.close(fig)


def test_max_per_row():
    """Test 2: max_per_row parameter"""
    print("\nTest 2: max_per_row parameter...")
    fig, ax = plt.subplots()
    for i in range(6):
        ax.plot([i, i+1, i+2], label=f"Line {i}")

    try:
        leg = ax.horizontal_legend(max_per_row=3)
        print(f"  - max_per_row=3: {leg._max_per_row}")
        assert leg._max_per_row == 3, "max_per_row should be 3"

        leg2 = ax.horizontal_legend(max_per_row=2)
        print(f"  - max_per_row=2: {leg2._max_per_row}")
        assert leg2._max_per_row == 2, "max_per_row should be 2"
        print("  [PASSED]")
    except Exception as e:
        print(f"  [FAILED]: {e}")
    finally:
        plt.close(fig)


def test_figure_integration():
    """Test 3: Integration with Figure"""
    print("\nTest 3: Figure.horizontal_legend()...")
    fig, axs = plt.subplots(1, 2)
    axs[0].plot([1, 2], label='A')
    axs[1].plot([2, 3], label='B')

    try:
        leg = fig.horizontal_legend(max_per_row=2)
        print(f"  - Type: {type(leg).__name__}")
        print(f"  - In figure legends: {leg in fig.legends}")
        labels = [t.get_text() for t in leg.get_texts()]
        print(f"  - Labels: {labels}")

        assert isinstance(leg, mlegend.HorizontalLegend), "Should be HorizontalLegend"
        assert leg in fig.legends, "Should be in figure legends"
        assert labels == ['A', 'B'], f"Labels should be ['A', 'B'], got {labels}"
        print("  [PASSED]")
    except Exception as e:
        print(f"  [FAILED]: {e}")
    finally:
        plt.close(fig)


def test_pyplot_integration():
    """Test 4: Integration with pyplot"""
    print("\nTest 4: plt.horizontal_legend()...")
    fig, ax = plt.subplots()
    plt.plot([1, 2, 3], label="Test 1")
    plt.plot([2, 3, 4], label="Test 2")

    try:
        leg = plt.horizontal_legend(max_per_row=2)
        print(f"  - Type: {type(leg).__name__}")
        print(f"  - max_per_row: {leg._max_per_row}")

        assert isinstance(leg, mlegend.HorizontalLegend), "Should be HorizontalLegend"
        assert leg._max_per_row == 2, "max_per_row should be 2"
        print("  [PASSED]")
    except Exception as e:
        print(f"  [FAILED]: {e}")
    finally:
        plt.close(fig)


def visual_test():
    """Visual test: Create a comparison figure"""
    print("\n\nCreating visual comparison...")
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    # Standard legend (column-wise)
    for i in range(6):
        ax1.plot([i, i+1], label=f"Item {i}")
    ax1.set_title("Standard Legend (ncols=3)\nColumn-wise: 0,2,4 / 1,3,5")
    ax1.legend(ncols=3, loc='upper center')
    ax1.set_ylim(0, 8)

    # Horizontal legend (row-wise)
    for i in range(6):
        ax2.plot([i, i+1], label=f"Item {i}")
    ax2.set_title("Horizontal Legend (max_per_row=3)\nRow-wise: 0,1,2 / 3,4,5")
    ax2.horizontal_legend(max_per_row=3, loc='upper center')
    ax2.set_ylim(0, 8)

    plt.tight_layout()
    output_file = 'horizontal_legend_comparison.png'
    plt.savefig(output_file, dpi=100, bbox_inches='tight')
    print(f"Saved to: {os.path.abspath(output_file)}")
    print("\nClose the window to continue...")
    plt.show()


def main():
    """Run all tests"""
    print("="*60)
    print("HORIZONTAL LEGEND TEST SUITE")
    print("="*60)

    all_passed = True
    try:
        test_basic()
        test_max_per_row()
        test_figure_integration()
        test_pyplot_integration()

        print("\n" + "="*60)
        print("ALL TESTS COMPLETED!")
        print("="*60)

        # Visual test
        print("\nRunning visual test...")
        visual_test()

    except Exception as e:
        print(f"\nERROR: {e}")
        import traceback
        traceback.print_exc()
        return 1

    return 0


if __name__ == '__main__':
    sys.exit(main())
