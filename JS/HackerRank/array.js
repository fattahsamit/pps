function getSecondLargest(nums) {
  let n = nums.length,
    a = 0,
    b = 0;
  for (let i = 0; i < n; i++) {
    if (nums[i] > a) {
      a = nums[i];
    }
  }
  for (let i = 0; i < n; i++) {
    if (nums[i] > b) {
      if (nums[i] == a) {
        continue;
      } else {
        b = nums[i];
      }
    }
  }
  return b;
}
