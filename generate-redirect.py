import os

dirs = ['components', 'getting-started', 'developers']

template = "<script>document.location = '/{}/{}/';</script>"

for check_dir in dirs:
    for path in os.listdir(os.path.join('public', check_dir)):
        check_path = os.path.join('public', check_dir, path)

        if os.path.isdir(check_path):
            new_path = os.path.join('source', check_dir, "{}.html".format(path))
            # print(template.format(check_dir, path))
            # print(new_path)
            with open(new_path, 'w') as outp:
                outp.write(template.format(check_dir, path))

# Generated
# source/components/alarm_control_panel.html
# source/components/alarm_control_panel.manual.html
# source/components/alarm_control_panel.mqtt.html
# source/components/arduino.html
# source/components/automation.html
# source/components/browser.html
# source/components/camera.foscam.html
# source/components/camera.generic.html
# source/components/configurator.html
# source/components/conversation.html
# source/components/device_sun_light_trigger.html
# source/components/device_tracker.html
# source/components/device_tracker.actiontec.html
# source/components/device_tracker.aruba.html
# source/components/device_tracker.asuswrt.html
# source/components/device_tracker.ddwrt.html
# source/components/device_tracker.geofancy.html
# source/components/device_tracker.luci.html
# source/components/device_tracker.mqtt.html
# source/components/device_tracker.netgear.html
# source/components/device_tracker.nmap_scanner.html
# source/components/device_tracker.owntracks.html
# source/components/device_tracker.snmp.html
# source/components/device_tracker.thomson.html
# source/components/device_tracker.tomato.html
# source/components/device_tracker.tplink.html
# source/components/device_tracker.ubus.html
# source/components/discovery.html
# source/components/downloader.html
# source/components/group.html
# source/components/history.html
# source/components/ifttt.html
# source/components/ifttt.manything.html
# source/components/introduction.html
# source/components/isy994.html
# source/components/keyboard.html
# source/components/light.html
# source/components/light.blinksticklight.html
# source/components/light.hue.html
# source/components/light.hyperion.html
# source/components/light.limitlessled.html
# source/components/light.rfxtrx.html
# source/components/light.tellstick.html
# source/components/light.vera.html
# source/components/light.wink.html
# source/components/logbook.html
# source/components/media_player.html
# source/components/media_player.cast.html
# source/components/media_player.denon.html
# source/components/media_player.firetv.html
# source/components/media_player.itunes.html
# source/components/media_player.kodi.html
# source/components/media_player.mpd.html
# source/components/media_player.plex.html
# source/components/media_player.emby.html
# source/components/media_player.sonos.html
# source/components/media_player.squeezebox.html
# source/components/modbus.html
# source/components/mqtt.html
# source/components/notify.html
# source/components/notify.file.html
# source/components/notify.instapush.html
# source/components/notify.nma.html
# source/components/notify.pushbullet.html
# source/components/notify.pushover.html
# source/components/notify.slack.html
# source/components/notify.smtp.html
# source/components/notify.syslog.html
# source/components/notify.telegram.html
# source/components/notify.xmpp.html
# source/components/rfxtrx.html
# source/components/scene.html
# source/components/script.html
# source/components/sensor.html
# source/components/sensor.arduino.html
# source/components/sensor.arest.html
# source/components/sensor.bitcoin.html
# source/components/sensor.command_sensor.html
# source/components/sensor.cpuspeed.html
# source/components/sensor.dht.html
# source/components/sensor.efergy.html
# source/components/sensor.forecast.html
# source/components/sensor.glances.html
# source/components/sensor.modbus.html
# source/components/sensor.mqtt.html
# source/components/sensor.mysensors.html
# source/components/sensor.openweathermap.html
# source/components/sensor.rest.html
# source/components/sensor.rfxtrx.html
# source/components/sensor.rpi_gpio.html
# source/components/sensor.sabnzbd.html
# source/components/sensor.swiss_public_transport.html
# source/components/sensor.systemmonitor.html
# source/components/sensor.tellstick.html
# source/components/sensor.temper.html
# source/components/sensor.time_date.html
# source/components/sensor.transmission.html
# source/components/sensor.vera.html
# source/components/sensor.wink.html
# source/components/sensor.worldclock.html
# source/components/shell_command.html
# source/components/simple_alarm.html
# source/components/sun.html
# source/components/switch.html
# source/components/switch.arduino.html
# source/components/switch.arest.html
# source/components/switch.command_switch.html
# source/components/switch.edimax.html
# source/components/switch.hikvision.html
# source/components/switch.modbus.html
# source/components/switch.mqtt.html
# source/components/switch.rest.html
# source/components/switch.rfxtrx.html
# source/components/switch.rpi_gpio.html
# source/components/switch.tellstick.html
# source/components/switch.transmission.html
# source/components/switch.vera.html
# source/components/switch.wemo.html
# source/components/switch.wink.html
# source/components/tellstick.html
# source/components/thermostat.html
# source/components/thermostat.heat_control.html
# source/components/thermostat.nest.html
# source/components/thermostat.radiotherm.html
# source/components/vera.html
# source/components/verisure.html
# source/components/wink.html
# source/components/zone.html
# source/components/zwave.html
# source/getting-started/android.html
# source/getting-started/automation.html
# source/getting-started/autostart.html
# source/getting-started/configuration.html
# source/getting-started/devices.html
# source/getting-started/presence-detection.html
# source/getting-started/troubleshooting.html
# source/getting-started/troubleshooting-configuration.html
# source/developers/add_new_platform.html
# source/developers/api.html
# source/developers/architecture.html
# source/developers/creating_components.html
# source/developers/credits.html
# source/developers/frontend.html
# source/developers/python_api.html
# source/developers/rest_api.html
# source/developers/website.html
