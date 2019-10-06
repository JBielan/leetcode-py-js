var defangIPaddr = function(address) {
	return address.split('.').join('[.]');
};