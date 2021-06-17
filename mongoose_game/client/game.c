#include <raylib.h>

#include "game.h"

struct GameData game_data;

void
testing()
{
    game_data.direction = "down";

    const int screenWidth = 640;
    const int screenHeight = 480;

    InitWindow(screenWidth, screenHeight, "new_game");

    Vector2 ballPosition = { (float)screenWidth/2, (float)screenHeight/2 };

    SetTargetFPS(60);

    while (!WindowShouldClose())
    {
        if (IsKeyDown(KEY_UP)) {
            ballPosition.y -= 4.0f;
            game_data.direction = "up";
        }
        if (IsKeyDown(KEY_DOWN)) {
            ballPosition.y += 4.0f;
            game_data.direction = "down";
        }
        if (IsKeyDown(KEY_LEFT)) {
            ballPosition.x -= 4.0f;
            game_data.direction = "left";
        }
        if (IsKeyDown(KEY_RIGHT)) {
            ballPosition.x += 4.0f;
            game_data.direction = "right";
        }

        BeginDrawing();
        ClearBackground(RAYWHITE);
        DrawCircleV(ballPosition, 50, BLACK);
        EndDrawing();
    }

    CloseWindow();
}