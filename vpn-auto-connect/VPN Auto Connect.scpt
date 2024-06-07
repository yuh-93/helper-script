on idle
    -- VPNの名前を設定します
    set VPNname to "VPN(sue)"
    -- VPN接続を試みる間隔（秒）を設定します
    set waitingSeconds to 30
    -- VPN接続を試みないWiFi SSIDを設定します
    set excludedSSIDs to {"wireless-5g", "wireless-2g","wlan"}
    
    -- 現在接続しているWiFiのSSIDを取得します
    set mySSID to {do shell script "/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport -I | awk '/ SSID/ {print substr($0, index($0, $2))}'"} as string
    
    -- SSIDが空の場合、待機時間を返して終了します
    if mySSID as string is equal to "" then
        return waitingSeconds
    end if
    
    -- 現在のSSIDが除外リストに含まれている場合、待機時間を返して終了します
    if excludedSSIDs contains mySSID then
        return waitingSeconds
    end if
    
    -- システム設定を操作します
    tell application "System Events"
        -- ネットワーク設定の現在の位置を操作します
        tell current location of network preferences
            -- 指定した名前のVPN接続を取得します
            set myConnection to the service VPNname
            -- VPN接続が存在する場合
            if myConnection is not null then
                -- VPNが接続されていない場合
                if current configuration of myConnection is not connected then
                    -- 通知を表示してVPN接続を開始します
                    display notification {"Connecting VPN: ", VPNname} as string
                    connect myConnection
                end if
            end if
        end tell
    end tell
    -- 待機時間を返します
    return waitingSeconds
end idle