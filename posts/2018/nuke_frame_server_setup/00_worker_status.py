from hiero.ui.nuke_bridge.FnNsFrameServer import frameServer
print [worker.address for worker in frameServer.getStatus(1).workerStatus]