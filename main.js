
const {app, BrowserWindow} = require('electron')
const path = require('path')
const {ipcMain} = require("electron")
let aggresiveTakeoverId = null;
let mainWindow;

function focusLoss(e){
  aggresiveTakeoverId = setInterval(aggresiveTakeover, 1);
}

function aggresiveTakeover(){
  if(!mainWindow.isFocused())
    mainWindow.focus()
  else{
    clearInterval(aggresiveTakeoverId)
  }
}

function AnnoyingAsHellConfig(w){
  w.webContents.on("before-input-event", (event, input) => {
    if( (input.alt && input.key == 'Tab'))
      event.preventDefault()
    console.log(input)
  })
	w.show()
  w.setFullScreen(true)
  w.setAlwaysOnTop(true)
  w.on("blur",focusLoss)
}

function createWindow () {
    mainWindow = new BrowserWindow({
    width: 1000,
    height: 1000,
    frame:false,
    webPreferences: {
      preload: path.join(__dirname, 'preload.js'),
      contextIsolation:false,
      nodeIntegration:true,
    }
  })
  // and load the index.html of the app.
  mainWindow.loadFile('src/firstpage.html')
  // AnnoyingAsHellConfig(mainWindow)
}

app.on("before-input-event", (event, input) => {
  console.log(input)
})

app.whenReady().then(() => {
  createWindow()
  app.on('activate', function () {
    if (BrowserWindow.getAllWindows().length === 0) createWindow()
  })
})


app.on('window-all-closed', function () {
  if (process.platform !== 'darwin') app.quit()
})



ipcMain.on("suicide", e => app.quit())