var isPalindrome = function(x) {
	return x.toString(10) === x.toString(10).split("").reverse().join("");
};