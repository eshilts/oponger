"""
All of our data models go here.

For details on how Google App Engine handles these, see:
http://code.google.com/appengine/docs/python/datastore/modelclass.html
"""
from google.appengine.ext import db
from locations import DC

class Player(db.Model):
  date = db.DateTimeProperty(auto_now_add=True)
  pseudonym = db.StringProperty(required=True)
  user = db.UserProperty(required=True)
  location = db.GeoPtProperty(default=DC['geoPt'])
  def __str__(self):
    return "[Psuedonym: %s, Nickname: %s]" % (self.pseudonym, self.user.nickname())


class Game(db.Model):
  created_date = db.DateTimeProperty(auto_now_add=True)
  completed_date = db.DateTimeProperty()
  """The player who created the game."""
  player_1 = db.ReferenceProperty(Player, collection_name='game_set_1')
  """The player who joined the game."""
  player_2 = db.ReferenceProperty(Player, collection_name='game_set_2')
  player_1_score = db.IntegerProperty()
  player_2_score = db.IntegerProperty()
  def __str__(self):
    return "[Player_1: %s, Player_2: %s, Created: %s]" % (self.player_1, self.player_2, self.created_date)
