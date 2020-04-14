from flask import Flask, request, render_template, jsonify, Response
from model.modal import Modal
import json
import jsons
from model.slackevent import SlackEvent
import pprint
import traceback
import urllib
import requests
from model.caster import Caster
from model.event import Event
from utils.ban import Ban
from utils.log import Log
import bots
from utils.post import Post
import time
import sched
import os
import asyncio
from model.user import User

hardDisableAllBots = False

def callAllBots(event, mongoClient, user, emotes, actionQueue):
  botList = sorted(list(filter(lambda name: not name.startswith("_"), dir(bots))))
  for bot in botList:
    try:
      callBot(bot, event, mongoClient, user, emotes, actionQueue)
    except Exception as error:
      pprint.pprint(error)
      print(traceback.format_exc())

def getAllEmotes():
  postData = {
    'token': os.environ.get('SECRET')
  }
  # print('https://slack.com/api/emoji.list?{}'.format(urllib.parse.urlencode(postData)))
  req = requests.get('https://slack.com/api/emoji.list?{}'.format(urllib.parse.urlencode(postData)))
  allEmotes = list(req.json().get('emoji').keys())
  return allEmotes

def convertCase(name):
  components = name.split('_')
  return''.join(x.title() for x in components)

def callBot(bot, originalEvent, client, user, emotes, actionQueue):
  if hardDisableAllBots:
    return
  moduleType = getattr(bots, bot)
  className = convertCase(bot)
  runner = getattr(moduleType, className)(originalEvent, client, user, emotes, actionQueue)
  return runner.safeRun()

def botConfigure(action, bot, value):
  if action not in ['frequency', 'target']:
    return 'Supported actions are frequency and target'
  if bot not in ['code']:
    return 'Supported bots are code'
  
  # client = MongoClient(os.environ.get('MONGO'))
  # client.slack.bots.update_one({'name': bot}, {'$set': {action: value}})
  return '{} bot {} set to {}'.format(bot, action, value
)