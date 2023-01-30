function getSecondLargest(nums) {
  let n = nums.length;
  let a = 0;
  for (let i = 0; i < n; i++) {
    if (nums[i] > a) {
      a = nums[i];
    }
    return a;
  }
}
