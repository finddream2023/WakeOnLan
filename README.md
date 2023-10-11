# WakeOnLan
基于Python实现的远程开机/远程唤醒/局域网唤醒

## 设计初衷
办公室电脑需要下班关机，下班后要加班找文件或者什么的，要用到办公室电脑。

## 使用方法
1、使用前请先修改代码里面的配置信息：比如模式`mode`、`iplist`（包括：姓名、IP地址、MAC地址）等参数。<br>
![](https://github.com/finddream2023/WakeOnLan/raw/main/%E7%A4%BA%E4%BE%8B%E5%9B%BE%E7%89%87/%E4%BD%BF%E7%94%A8%E5%89%8D%E8%AF%B7%E5%85%88%E4%BF%AE%E6%94%B9%E9%85%8D%E7%BD%AE.png)<br><br>
2、直接双击运行py文件，或者执行命令行：`python WakeOnLan.py`<br>
示例结果输出为：Done，张三，132.115.122.101，4f-d1-9a-62-c0-f6<br>
![](https://github.com/finddream2023/WakeOnLan/raw/main/%E7%A4%BA%E4%BE%8B%E5%9B%BE%E7%89%87/%E6%89%A7%E8%A1%8C%E7%BB%93%E6%9E%9C%E7%A4%BA%E4%BE%8B.png)<br>

## 电脑设置
执行后如果电脑不能正常开机的，需要先做一下设置：<br><br>
1、【控制面板=》电源选项】，设置电源按钮那个界面，取消“快速启动”（貌似win10开始的才需要）<br>
![](https://github.com/finddream2023/WakeOnLan/raw/main/%E7%A4%BA%E4%BE%8B%E5%9B%BE%E7%89%87/%E7%94%B5%E6%BA%90%E8%AE%BE%E7%BD%AE.png)<br><br>
2、【控制面板=》网络和共享中心】，网卡属性配置=》电源管理，取消“允许关闭设备”，勾选2个允许唤醒计算机<br>
实测这里有个坑，要先同时选择3项确定，再重进取消第1项<br>
![](https://github.com/finddream2023/WakeOnLan/raw/main/%E7%A4%BA%E4%BE%8B%E5%9B%BE%E7%89%87/%E7%BD%91%E5%8D%A1%E8%AE%BE%E7%BD%AE.png)<br><br>
3、【BIOS】设置允许wake on LAN；resume on lan；power on PME；power on by PCI-E device; Power on by Onboard LAN等字眼的<br>

