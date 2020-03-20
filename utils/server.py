from flask import Flask, request, render_template, jsonify, Response
from model.modal import Modal
from multiprocessing import Pool
from constant.channels import CHANNELS
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

def getAllEmotes():
  postData = {
    'token': os.environ.get('SECRET')
  }
  req = requests.get('https://slack.com/api/emoji.list?{}'.format(urllib.parse.urlencode(postData)))
  allEmotes = list(req.json().get('emoji').keys())
  return allEmotes

def convertCase(name):
  components = name.split('_')
  return''.join(x.title() for x in components)

def callBot(bot, originalEvent, pool, client, user, emotes):
  moduleType = getattr(bots, bot)
  className = convertCase(bot)
  runner = getattr(moduleType, className)(originalEvent, pool, client, user)
  return runner.run()

def botConfigure(action, bot, value):
  if action not in ['frequency', 'target']:
    return 'Supported actions are frequency and target'
  if bot not in ['code']:
    return 'Supported bots are code'
  
  # client = MongoClient(os.environ.get('MONGO'))
  # client.slack.bots.update_one({'name': bot}, {'$set': {action: value}})
  return '{} bot {} set to {}'.format(bot, action, value)