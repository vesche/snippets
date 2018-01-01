function love.load()
    x = 50
    y = 50
end

function love.update()
    if love.keyboard.isDown("right") then
        x = x + 1
    end
    if love.keyboard.isDown("left") then
        x = x - 1
    end
    if love.keyboard.isDown("up") then
        y = y - 1
    end
    if love.keyboard.isDown("down") then
        y = y + 1
    end
end

function love.draw()
    love.graphics.setColor(0, 0, 255)
    love.graphics.rectangle("fill", x, y, 100, 100)
end
