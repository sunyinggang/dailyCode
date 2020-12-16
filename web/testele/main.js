const { app, BrowserWindow,dialog } = require('electron')

// 热加载
try {
    require('electron-reloader')(module,{});
} catch (_) {}

function createWindow () {
    const win = new BrowserWindow({
        width: 800,
        height: 1000,
        autoHideMenuBar: true,
        webPreferences: {
            nodeIntegration: true
        }
    })

    win.loadFile('index.html')
}

app.whenReady().then(createWindow)

app.on('window-all-closed', () => {
    if (process.platform !== 'darwin') {
        app.quit()
    }
})

app.on('activate', () => {
    if (BrowserWindow.getAllWindows().length === 0) {
        createWindow()
    }
})

const fs = require('fs')
const xlsx = require('xlsx')
const {ipcMain} = require('electron')

// const root = fs.readdirSync(__dirname)
// console.log(root)
ipcMain.handle('ping', (evidence, ...args) => {
    console.log('got ping', args)
})



