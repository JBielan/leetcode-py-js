var twoSum = function(nums, target) {
   let memory = new Map();      // memory' will store met numbers along with indexes to prevent iterating multiple times
   for (let i = 0; i < nums.length; i++) {      // for every possible nums index i
	   if (memory.has(target - nums[i])) {      // if seeking number has already been visited and is stored in memory
		   return [memory.get(target-nums[i]), i];      // just return an index of this number along with current index
	   }
	   else {
		   memory.set(nums[i], i);      // otherwise add the number to memory along with index
	   }
   }
	return [];      // in case the loop is exited, just return an empty array
};