class Solution {
  public int searchInsert(int[] nums, int target) {
    int a = 0;
    int b = nums.length;

    while (a < b) {
      final int m = (a + b) / 2;
      if (nums[m] == target)
        return m;
      if (nums[m] < target)
        a = m + 1;
      else
        b = m;
    }

    return a;
  }
}
