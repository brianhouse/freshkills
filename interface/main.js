let img
let tick = 0
let start
let elapsed
let pos
let duration
let h

function setup() {
    createCanvas(windowWidth, windowHeight)            
    // img = loadImage('../roberts_scores/seasonal_vegetation.jpg')
    img = loadImage('../roberts_scores/monthly_tides.jpg')
    // img = loadImage('../scores/lifetime_climate.png')    
    start = millis()
    // 10 mins + 20sec intro + 20 sec outro + 1min random
    duration = (10 * 60 * 1000) + (26 * 1000) + (26 * 1000)// + (random() * 60 * 1000)
    frameRate(10)
    fill(0, 0, 0, 100)    
}

function windowResized() {
    resizeCanvas(windowWidth, windowHeight)
}

function draw() {
    background(255)
    elapsed = millis() - start    
    pos = elapsed / duration
    h = (windowWidth / 16) * 9
    image(img, 0, (windowHeight / 2) - (h / 2), windowWidth, h)
    noStroke()
    rect(0, 0, pos * windowWidth, windowHeight)
    tick += 1
}

function touchStarted() {
    fill(0, 0, 0, 100)    
    start = millis()
}
