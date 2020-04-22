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
  'C011WA7AFQE': {'post': True, 'name': 'CivilizationTwoFrontWar'},
  'C011NA88LVD': {'post': True, 'name': 'civ_lack_game'},
  'C011S05A3SB': {'post': True, 'name': 'civ_hide_from_sumeria'},
  'C012AAM0FNZ': {'post': True, 'name': 'Alerts'}
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

def civHideFromSumeria():
  return 'C011S05A3SB'

def alertsChannel():
  return 'C012AAM0FNZ'

def allowed_channel_ids():
  allowedChannels = list(filter(lambda channelObj: channelObj[1].get('post'), CHANNELS.items()))
  return list(map(lambda x: x[0], allowedChannels))
