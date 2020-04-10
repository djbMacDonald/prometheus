ALLOWED_CHANNELS = {
  'CDU145F08',
  'CDR5ZBTT7',
  'CH0TUPU6R',
  'CMNCA7EV7'
}

CHANNELS = {
  'Megamoji': 'CDU145F08',
  'Chaos':'CDR5ZBTT7',
  'Reminders': 'CGFSDDPTQ',
  'Schemes': 'CDBT6UTCL',
  'Secret': 'CH0TUPU6R',
  'Underscore': 'CMNCA7EV7'
}

NEW_CHANNEL_OBJECT = {
  'CDU145F08': {'post': True, 'name': 'Megamoji'},
  'CDR5ZBTT7': {'post': True, 'name': 'Chaos'},
  'CH0TUPU6R': {'post': True, 'name': 'Secret'},
  'CMNCA7EV7': {'post': True, 'name': 'Underscore'},
  'CGFSDDPTQ': {'post': False, 'name': 'Reminders'},
  'CDBT6UTCL': {'post': False, 'name': 'Schemes'}
}

def allowed_channel_ids():
  allowedChannels = list(filter(lambda channelObj: channelObj[1].get('post'), NEW_CHANNEL_OBJECT.items()))
  return list(map(lambda x: x[0], allowedChannels))
