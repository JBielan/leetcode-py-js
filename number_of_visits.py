class Solution:
	def subdomainVisits(self, cpdomains):
		count = {}      # this dictionary will store subdomains with the number of visits
		for domain in cpdomains:        # let's split subdomains and visits
			item = domain.split(' ')        # separate visits from a domain
			visits = int(item[0])       # first item is a number of visits
			whole_domain = item[1]       # and the second item is a whole domain
			whole_domain = whole_domain.split('.')      # to iterate let's split it when commas
			subdomains = []
			for i in range(len(whole_domain)):
				subdomains.append('.'.join(whole_domain[i:]))       # create subdomains by cutting them from the left

			# when we've got all subdomains, it's enough to add visits to the count dictionary
			for subdomain in subdomains:
				if subdomain not in count:      # if there isn't any occurance, just treat as zero - you could use default dictionary as well
					count[subdomain] = 0

				count[subdomain] += visits      # add the number of visits

		# right now the last thing is to make a transition to a list
		result = []
		for key in count:
			result.append("{} {}".format(count[key], key))      # put the number of visits together with subdomain and add it to the results

		return result
