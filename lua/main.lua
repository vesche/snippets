function love.load()
    x = 200
end

function love.update(dt)
    if love.keyboard.isDown("right") then
        if x < 720 then
            x = x + 6
        end
    end
    if love.keyboard.isDown("left") then
        if x > 0 then
            x = x - 6
        end
    end
end

function love.draw()
    love.graphics.setColor(0, 100, 255)
    love.graphics.rectangle("fill", x, 500, 80, 20)
end
