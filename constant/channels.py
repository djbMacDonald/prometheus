CHANNELS = {
  'CDU145F08': {'post': True, 'name': 'Megamoji'},
  'CDR5ZBTT7': {'post': True, 'name': 'Chaos'},
  'CH0TUPU6R': {'post': True, 'name': 'Secret'},
  'CMNCA7EV7': {'post': True, 'name': 'Underscore'},
  'CGFSDDPTQ': {'post': False, 'name': 'Reminders'},
  'CDBT6UTCL': {'post': False, 'name': 'Schemes'},
  'C011E259FR8': {'post': True, 'name': 'Civilization'},
  'C012EG6BF9N': {'post': True, 'name': 'CivilizationSlaughter'},
  'C011XG78YM8': {'post': True, 'name': 'CivilizationBeerdeau'},
  'C011WA7AFQE': {'post': True, 'name': 'CivilizationTwoFrontWar'}
}

def chaosChannel():
  return 'CDR5ZBTT7'

def underscoreChannel():
 return 'CMNCA7EV7'

def civChannel():
  return 'C011E259FR8'

def civSlaughterChannel():
  return 'C012EG6BF9N'

def civBeerdeauChannel():
  return 'C011XG78YM8'

def civTwoFrontWarChannel():
  return 'C011WA7AFQE'

def civLackChannel():
  return 'C011NA88LVD'

def allowed_channel_ids():
  allowedChannels = list(filter(lambda channelObj: channelObj[1].get('post'), CHANNELS.items()))
  return list(map(lambda x: x[0], allowedChannels))
