from datetime import datetime, timedelta
import json
import requests


SUBDOMAIN='COMPANY'
API_ACCESS_KEY='REDACTED'


def trigger_incident(message):
    headers = {
        'Authorization': 'Token token={0}'.format(API_ACCESS_KEY),
        'Content-type': 'application/json',
    }
    payload = json.dumps({
      "service_key": "69db0f2ec04b413c913c3d7a14f8c559",
      "event_type": "trigger",
      "description": message,
      "client": "API",
      "client_url": "https://www.devero.com",
      "details": {
        "ping time": "1500ms",
        "load avg": 0.75
      }
    })
    r = requests.post(
                    'https://events.pagerduty.com/generic/2010-04-15/create_event.json',
                    headers=headers,
                    data=payload,
    )
    print r.status_code
    print r.text


def create_maintenance_window(environment_name):
  url = 'https://COMPANY.pagerduty.com/api/v1/maintenance_windows'
  # This uses the v1 API.
  api_access_key = 'REDACTED'
  service_ids = ['PYGEN3X']
  """ Get the current time in PagerDuty-friendly UTC offset time format (<YYYY>-<MM>-<DD>T<hh>:<mm>:<ss>-<oo:oo>Z): """
  start_time = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%SZ")
  """ Calculate the end time: """
  """ Set the window for six hours, which should be enough time... we'll be deleting it at the end of this script anyways.
    There may be instances in the future where we'll need a window longer than six hours to complete this, depending on
    sleep time and number of instances.  In that case, just increase the number of hours below. """
  end_time = (datetime.utcnow() + timedelta(hours=6)).strftime("%Y-%m-%d %H:%M:%SZ")
  """ Create the JSON to send to PagerDuty """
  headers = {
        'Authorization': 'Token token={0}'.format(api_access_key),
        'Content-type': 'application/json',
  }
  payload = {
      "maintenance_window": {
          'start_time': start_time,
          'end_time': end_time,
          "description": 'Maintenance mode for {0}.'.format(environment_name),
          "service_ids": service_ids,
      }
  }
  request = requests.post(url, headers=headers, data=json.dumps(payload))
  parsed_response = json.loads(request.text)
  print(json.dumps(parsed_response, indent=2))
  return parsed_response['maintenance_window']['id']


def delete_maintenance_window(maintenance_id):
  url = 'https://COMPANY.pagerduty.com/api/v1/maintenance_windows'
  # This uses the v1 API.
  api_access_key = 'REDACTED'
  headers = {
        'Authorization': 'Token token={0}'.format(api_access_key),
        'Content-type': 'application/json',
  }
  request = requests.delete(url + '/' + maintenance_id, headers=headers)
  print(request.text)
  print("Deleted PagerDuty maintenance window %s for Unhealthy Host Count service." % maintenance_id)
  return
