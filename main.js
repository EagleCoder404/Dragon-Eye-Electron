
const {app, BrowserWindow} = require('electron')
const path = require('path')

let mainWindow;

function createWindow () {
    mainWindow = new BrowserWindow({
    width: 600,
    height: 300,
    frame:false,
    webPreferences: {
      preload: path.join(__dirname, 'preload.js'),
      contextIsolation:false,
      nodeIntegration:true,
    }
  })


  mainWindow.loadFile('src/login.html')
}


app.whenReady().then(() => {
  createWindow()
  app.on('activate', function () {
    if (BrowserWindow.getAllWindows().length === 0) createWindow()
  })
})


app.on('window-all-closed', function () {
  if (process.platform !== 'darwin') app.quit()
})



