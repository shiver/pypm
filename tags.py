_tags	= {}		# holds the tag names
_tagged = {}		# holds the tag-to-external_reference associations

def add_tag(tagname, external_reference):
	"""
	Creates a tag with the specified tagname and associates
	it with the supplied external_reference (which should be an id)

	Returns the tag id if successful, otherwise None
	"""
	
	# create or retrieve tag id
	tag_id = _create_tag(tagname)

	# if for some reason we couldn't get a tag id
	# jump out now
	if tag_id is None:
		return None
	
	# if there are no associations for the tag_id yet,
	# add it 
	if not _tagged.has_key(tag_id):
		_tagged[tag_id] = [external_reference]
	else:
		# append the external reference to the existing list
		if not external_reference in _tagged[tag_id]:
			_tagged[tag_id] += [external_reference]

	return tag_id

def _create_tag(tagname):
	"""
	Note: Called by add_tag(). Not to be called directly

	Either creates or retrieves the id of a tag with specified
	by tagname

	Returns the tag id if successful, otherwise None
	"""

	if _tags != None:
		tag_id = 0
		if len(_tags):
			# does tag exist already?
			for id, name in _tags.items():
				if name == tagname:
					return id
			tag_id = max(_tags) + 1
		_tags[tag_id] = tagname
		return tag_id
	return None

def remove_tag(id=None, tagname=None):
	"""
	Remove a tag
	id - if supplied will be preferred over tag name
	tagname - if no id supplied, will remove based on name

	Returns True if successful, otherwise False
	"""

	if id is None and tagname is None:
		return False

	# prefer by id if we have it
	if id != None:
		if _tags.has_key(id):
			# delete associations
			if _tagged.has_key(id):
				del(_tagged[id])
			# delete the actual tag
			del(_tags[id])
			return True
		return False
	# otherwise, use the tagname
	else: 
		if tagname:
			for id, name in _tags.items():
				if name == tagname:
					# delete associations
					if _tagged.has_key(id):
						del(_tagged[id])
					# delete the actual tag
					del(_tags[id])
					return True
		else:
			return False

	return False

def find_tag(tagname, case_sensitive=True):
	"""
	Find the tag which contains tagname

	Returns a list of tag ids which contain the supplied tagname
	"""

	matches = []
	if tagname is None:
		return matches

	if not case_sensitive:
		tagname = tagname.lower()	# so we dont call it in the for loop
									# should be a little quicker
	
	for id, name in _tags.iteritems():
		if not case_sensitive:
			name = name.lower()

		if tagname in name:
			matches.append(id)

	return matches

def get_linked_tags(external_reference):
	"""
	Returns a list of all the tags associated with the 
	specified external_reference
	"""

	matches = []

	for id, refs in _tagged.iteritems():
		if external_reference in refs:
			matches += [id]

	return matches

def get_name(tag_id):
	"""
	Returns the name of the specified tag id, otherwise None
	"""

	if tag_id == None:
		return None

	if _tags.has_key(tag_id):
		return _tags[tag_id]

	return None

def get_tag_names():
	"""
	Retrieves all tag names
	"""

	return _tags.values()
