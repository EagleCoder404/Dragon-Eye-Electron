
const {app, BrowserWindow} = require('electron')
const screenshot = require("screenshot-desktop")
const path = require('path')
const fs = require("fs")
const {ipcMain} = require("electron")

let aggresiveTakeoverId = null;
let mainWindow;



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
  init()
  mainWindow.loadFile('src/firstpage.html')
  // AnnoyingAsHellConfig(mainWindow)
}

function init(){

}

function AnnoyingAsHellConfig(w){
  // w.webContents.on("before-input-event", (event, input) => {
  //   if( (input.alt && input.key == 'Tab'))
  //   event.preventDefault()
  //   console.log(input)
  // })
  w.show()
  w.setFullScreen(true)
  w.setAlwaysOnTop(true)
  w.on("blur",focusLoss)
}

function begone(w){
  w.removeListener("blur", focusLoss)
  w.setFullScreen(false)
  w.setAlwaysOnTop(false)
}

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







app.whenReady().then(() => {
  createWindow()
  app.on('activate', function () {
    if (BrowserWindow.getAllWindows().length === 0) createWindow()
  })
})

app.on('window-all-closed', function () {
  if (process.platform !== 'darwin') app.quit()
})

function endExam(){
  app.quit()
}

ipcMain.on("suicide", e => app.quit())

ipcMain.on("start-exam", (e, token) => {

  mainWindow.on("blur", screenshot_it)
  AnnoyingAsHellConfig(mainWindow)

})

ipcMain.on("end-exam", e => {
  begone(mainWindow)
  mainWindow.removeListener("blur", screenshot_it)
  mainWindow.unmaximize()
}) 

ipcMain.on("set-exam-timeout", (e, et) => {
  const end_time = new Date(et)
  const current_time = new Date()
  console.log(end_time, current_time)
  console.log("App will time out at " + ((end_time - current_time)/1000/60) + " minutes")
  setTimeout(endExam, end_time - current_time)
})

function screenshot_it(e, token) {
    const file_path = path.resolve("facial", "screenshots", `${token}_${Date()}.png`)
    fs.appendFileSync(file_path, "", (e, d) => {if(e) console.log(e)})
    screenshot({filename: file_path})
}