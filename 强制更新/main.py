import frida
import sys

rdev = frida.get_remote_device()
pid = rdev.spawn(["com.hupu.shihuo"])
session = rdev.attach(pid)

scr = """
Java.perform(function () {
    var UpdateDialog = Java.use('com.azhon.appupdate.dialog.UpdateDialog');
    UpdateDialog.show.implementation = function(ctx){
        //this.show();
    }
});
"""
script = session.create_script(scr)


def on_message(message, data):
    print(message, data)


script.on("message", on_message)
script.load()
rdev.resume(pid)
sys.stdin.read()
