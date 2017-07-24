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

    if (window == NULL) {
        printf("error create window: %s\n", SDL_GetError());
        SDL_Quit();
        return 1;
    }

    // create renderer
    renderer = SDL_CreateRenderer(window, -1, SDL_RENDERER_ACCELERATED);

    if (renderer == NULL) {
        printf("error create renderer: %s\n", SDL_GetError());
        SDL_DestroyWindow(window);
        SDL_Quit();
        return 1;
    }

    // load image into mem
    surface = IMG_Load("ball.jpg");

    if (surface == NULL) {
        printf("error create surface: %s\n", SDL_GetError());
        SDL_DestroyRenderer(renderer);
        SDL_DestroyWindow(window);
        SDL_Quit();
        return 1;
    }

    // load image into graphics hardware mem
    texture = SDL_CreateTextureFromSurface(renderer, surface);
    SDL_FreeSurface(surface); // release surface from mem

    if (texture == NULL) {
        printf("error create texture: %s\n", SDL_GetError());
        SDL_DestroyRenderer(renderer);
        SDL_DestroyWindow(window);
        SDL_Quit();
        return 1;
    }

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
