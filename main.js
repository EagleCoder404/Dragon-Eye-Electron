
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

<<<<<<< HEAD
  // and load the index.html of the app.
  mainWindow.loadFile('src/firstpage.html')
  mainWindow.webContents.openDevTools()
  mainWindow.setFullScreen(true)
	mainWindow.show()
  // and load the index.html of the app.
=======
>>>>>>> 0c44fb8e2083a2843d5d857de509e7c9d1136367

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



