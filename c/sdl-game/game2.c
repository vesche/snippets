/*
 * test.c
 */

#include <stdio.h>
#include <SDL2/SDL.h>
#include <SDL2/SDL_image.h>

int main(void)
{
    // declare pointers
    SDL_Window *window;
    SDL_Renderer *renderer;
    SDL_Surface *surface;
    SDL_Texture *texture;

    if (SDL_Init(SDL_INIT_EVERYTHING) != 0)
    {
        printf("error SDL init: %s\n", SDL_GetError());
        return 1;
    }
    printf("init success\n");

    // create window
    window = SDL_CreateWindow(
        "PokeClone",
        SDL_WINDOWPOS_UNDEFINED,
        SDL_WINDOWPOS_UNDEFINED,
        640, 480, 0);

    // create renderer
    renderer = SDL_CreateRenderer(window, -1, SDL_RENDERER_ACCELERATED);

    // load image into mem
    surface = IMG_Load("ball.jpg");

    // load image into graphics hardware mem
    texture = SDL_CreateTextureFromSurface(renderer, surface);
    SDL_FreeSurface(surface); // release surface from mem

    // clear the window
    SDL_RenderClear(renderer);

    // draw image to screen
    SDL_RenderCopy(renderer, texture, NULL, NULL);
    SDL_RenderPresent(renderer);

    // wait 10 seconds
    SDL_Delay(10000);

    // close and destroy texture, renderer, window
    SDL_DestroyTexture(texture);
    SDL_DestroyRenderer(renderer);
    SDL_DestroyWindow(window);

    // clean up
    SDL_Quit();
    return 0;
}
