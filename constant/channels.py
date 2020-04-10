CHANNELS = {
  'CDU145F08': {'post': True, 'name': 'Megamoji'},
  'CDR5ZBTT7': {'post': True, 'name': 'Chaos'},
  'CH0TUPU6R': {'post': True, 'name': 'Secret'},
  'CMNCA7EV7': {'post': True, 'name': 'Underscore'},
  'CGFSDDPTQ': {'post': False, 'name': 'Reminders'},
  'CDBT6UTCL': {'post': False, 'name': 'Schemes'}
}

def chaosChannel():
  return 'CDR5ZBTT7'

def underscoreChannel():
 return 'CMNCA7EV7'

def allowed_channel_ids():
  allowedChannels = list(filter(lambda channelObj: channelObj[1].get('post'), CHANNELS.items()))
  return list(map(lambda x: x[0], allowedChannels))
