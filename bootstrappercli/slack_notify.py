import json
import urllib

SLACK_WEBHOOK = "https://bootstrapper.slack.com/services/hooks/incoming-webhook?token=abcdefghijklmnopqrstuvwxyz"

def post_hook(bs_user, bs_action, ans_env, ans_role):
  if ans_env == "dev":
    ans_env = "staging"
  msg = {
        "channel": "#bootstrapper",
        "username": "bootstrappercli",
        "text": "%s invoked %s via bootstrappercli on %s:%s" %(bs_user, bs_action, ans_env, ans_role),
        "icon_emoji": "cubimal_chick"
        }
  data = urllib.urlencode({"payload": json.dumps(msg)})
  response = urllib.urlopen(SLACK_WEBHOOK, data).read()
  return response
