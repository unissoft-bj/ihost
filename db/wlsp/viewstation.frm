TYPE=VIEW
query=select `wlsp`.`wlsta`.`id` AS `id`,`wlsp`.`wlsta`.`mac` AS `mac`,`wlsp`.`wlsta`.`firstseen` AS `firstseen`,`wlsp`.`wlsta`.`lastseen` AS `lastseen`,`wlsp`.`wlsta`.`ssid` AS `ssid`,`wlsp`.`wlsta`.`rssi` AS `rssi`,`wlsp`.`wlsta`.`stat` AS `stat`,`wlsp`.`wlsta`.`npacket` AS `npacket`,`wlsp`.`wlsta`.`action` AS `action` from `wlsp`.`wlsta`
md5=b29c0b67b882513077852ee34cac8e2f
updatable=1
algorithm=0
definer_user=root
definer_host=%
suid=1
with_check_option=0
timestamp=2014-11-11 13:35:18
create-version=1
source=select `wlsta`.`id` AS `id`,`wlsta`.`mac` AS `mac`,`wlsta`.`firstseen` AS `firstseen`,`wlsta`.`lastseen` AS `lastseen`,`wlsta`.`ssid` AS `ssid`,`wlsta`.`rssi` AS `rssi`,`wlsta`.`stat` AS `stat`,`wlsta`.`npacket` AS `npacket`,`wlsta`.`action` AS `action` from `wlsta`
client_cs_name=latin1
connection_cl_name=latin1_swedish_ci
view_body_utf8=select `wlsp`.`wlsta`.`id` AS `id`,`wlsp`.`wlsta`.`mac` AS `mac`,`wlsp`.`wlsta`.`firstseen` AS `firstseen`,`wlsp`.`wlsta`.`lastseen` AS `lastseen`,`wlsp`.`wlsta`.`ssid` AS `ssid`,`wlsp`.`wlsta`.`rssi` AS `rssi`,`wlsp`.`wlsta`.`stat` AS `stat`,`wlsp`.`wlsta`.`npacket` AS `npacket`,`wlsp`.`wlsta`.`action` AS `action` from `wlsp`.`wlsta`
