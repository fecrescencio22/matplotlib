#!/usr/bin/env python
"""
Manual test script for horizontal_legend feature.
Run this to verify your implementation is working correctly.
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.legend as mlegend

def test_basic():
    """Test 1: Basic functionality"""
    print("Test 1: Basic horizontal_legend creation...")
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3], label="Line 1")
    ax.plot([2, 3, 4], label="Line 2")
    ax.plot([3, 4, 5], label="Line 3")

    leg = ax.horizontal_legend()

    assert isinstance(leg, mlegend.HorizontalLegend), "Should create HorizontalLegend instance"
    assert len(leg.get_texts()) == 3, "Should have 3 legend entries"
    assert leg._max_per_row == 4, "Default max_per_row should be 4"
    print("✓ PASSED\n")
    plt.close(fig)


def test_max_per_row():
    """Test 2: max_per_row parameter"""
    print("Test 2: max_per_row parameter...")
    fig, ax = plt.subplots()
    for i in range(6):
        ax.plot([i, i+1, i+2], label=f"Line {i}")

    leg = ax.horizontal_legend(max_per_row=3)
    assert leg._max_per_row == 3, "max_per_row should be 3"

    leg2 = ax.horizontal_legend(max_per_row=2)
    assert leg2._max_per_row == 2, "max_per_row should be 2"
    print("✓ PASSED\n")
    plt.close(fig)


def test_axes_integration():
    """Test 3: Integration with Axes"""
    print("Test 3: Axes.horizontal_legend()...")
    fig, ax = plt.subplots()
    ax.plot([1, 2], [3, 4], label='A')
    ax.plot([2, 3], [4, 5], label='B')

    leg = ax.horizontal_legend(max_per_row=2)

    assert isinstance(leg, mlegend.HorizontalLegend), "Should be HorizontalLegend"
    assert ax.get_legend() is leg, "Should be set as axes legend"
    labels = [t.get_text() for t in leg.get_texts()]
    assert labels == ['A', 'B'], f"Labels should be ['A', 'B'], got {labels}"
    print("✓ PASSED\n")
    plt.close(fig)


def test_figure_integration():
    """Test 4: Integration with Figure"""
    print("Test 4: Figure.horizontal_legend()...")
    fig, axs = plt.subplots(1, 2)
    axs[0].plot([1, 2], label='A')
    axs[1].plot([2, 3], label='B')

    leg = fig.horizontal_legend(max_per_row=2)

    assert isinstance(leg, mlegend.HorizontalLegend), "Should be HorizontalLegend"
    assert leg in fig.legends, "Should be in figure legends"
    labels = [t.get_text() for t in leg.get_texts()]
    assert labels == ['A', 'B'], f"Labels should be ['A', 'B'], got {labels}"
    print("✓ PASSED\n")
    plt.close(fig)


def test_pyplot_integration():
    """Test 5: Integration with pyplot"""
    print("Test 5: plt.horizontal_legend()...")
    fig, ax = plt.subplots()
    plt.plot([1, 2, 3], label="Test 1")
    plt.plot([2, 3, 4], label="Test 2")

    leg = plt.horizontal_legend(max_per_row=2)

    assert isinstance(leg, mlegend.HorizontalLegend), "Should be HorizontalLegend"
    assert leg._max_per_row == 2, "max_per_row should be 2"
    print("✓ PASSED\n")
    plt.close(fig)


def test_custom_labels():
    """Test 6: Custom labels"""
    print("Test 6: Custom labels...")
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3])
    ax.plot([2, 3, 4])

    leg = ax.horizontal_legend(['Custom A', 'Custom B'], max_per_row=2)

    labels = [t.get_text() for t in leg.get_texts()]
    assert labels == ['Custom A', 'Custom B'], f"Expected ['Custom A', 'Custom B'], got {labels}"
    print("✓ PASSED\n")
    plt.close(fig)


def test_kwargs():
    """Test 7: Other kwargs pass-through"""
    print("Test 7: Kwargs pass-through...")
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3], label="Test")

    leg = ax.horizontal_legend(
        max_per_row=2,
        loc='upper right',
        frameon=True,
        shadow=True,
        title='Test Title'
    )

    assert leg.get_title().get_text() == 'Test Title', "Title should be set"
    print("✓ PASSED\n")
    plt.close(fig)


def test_ncols_ignored():
    """Test 8: ncols parameter is ignored"""
    print("Test 8: ncols parameter ignored...")
    fig, ax = plt.subplots()
    for i in range(4):
        ax.plot([i, i+1], label=f"Line {i}")

    leg = ax.horizontal_legend(max_per_row=2, ncols=3)

    assert leg._max_per_row == 2, "max_per_row should be 2"
    assert leg._ncols == 2, "ncols should match max_per_row, not the passed ncols"
    print("✓ PASSED\n")
    plt.close(fig)


def test_remove():
    """Test 9: Remove legend"""
    print("Test 9: Remove horizontal_legend...")
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3], label="Test")

    leg = ax.horizontal_legend()
    leg.remove()

    assert ax.get_legend() is None, "Legend should be removed"
    print("✓ PASSED\n")
    plt.close(fig)


def test_many_items():
    """Test 10: Many items with wrapping"""
    print("Test 10: Many items with wrapping...")
    fig, ax = plt.subplots()
    n_items = 10
    for i in range(n_items):
        ax.plot([i, i+1], label=f"Item {i}")

    leg = ax.horizontal_legend(max_per_row=3)

    assert len(leg.get_texts()) == n_items, f"Should have {n_items} labels"
    assert leg._max_per_row == 3, "max_per_row should be 3"
    print("✓ PASSED\n")
    plt.close(fig)


def visual_test():
    """Visual test: Create a comparison figure"""
    print("\nCreating visual comparison test...")
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    # Standard legend (column-wise)
    for i in range(6):
        ax1.plot([i, i+1], label=f"Item {i}")
    ax1.set_title("Standard Legend (ncols=3)\nColumn-wise filling: 0,2,4 / 1,3,5")
    ax1.legend(ncols=3, loc='upper center')

    # Horizontal legend (row-wise)
    for i in range(6):
        ax2.plot([i, i+1], label=f"Item {i}")
    ax2.set_title("Horizontal Legend (max_per_row=3)\nRow-wise filling: 0,1,2 / 3,4,5")
    ax2.horizontal_legend(max_per_row=3, loc='upper center')

    plt.tight_layout()
    plt.savefig('horizontal_legend_comparison.png', dpi=100, bbox_inches='tight')
    print("✓ Saved comparison figure to 'horizontal_legend_comparison.png'\n")
    plt.show()


def main():
    """Run all tests"""
    print("="*60)
    print("HORIZONTAL LEGEND TEST SUITE")
    print("="*60 + "\n")

    try:
        test_basic()
        test_max_per_row()
        test_axes_integration()
        test_figure_integration()
        test_pyplot_integration()
        test_custom_labels()
        test_kwargs()
        test_ncols_ignored()
        test_remove()
        test_many_items()

        print("="*60)
        print("✓ ALL TESTS PASSED!")
        print("="*60 + "\n")

        # Ask if user wants to see visual test
        response = input("Would you like to run the visual test? (y/n): ")
        if response.lower() == 'y':
            visual_test()

    except AssertionError as e:
        print(f"\n✗ TEST FAILED: {e}")
        return 1
    except Exception as e:
        print(f"\n✗ ERROR: {e}")
        import traceback
        traceback.print_exc()
        return 1

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main())
