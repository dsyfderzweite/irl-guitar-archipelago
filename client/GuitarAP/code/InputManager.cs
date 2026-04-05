using Microsoft.Xna.Framework.Input;
using Microsoft.Xna.Framework;

namespace GuitarAP;

public static class InputManager{
    private static MouseState previousMouseState;
    private static MouseState currentMouseState;

    private static KeyboardState previousKeyboardState;
    private static KeyboardState currentKeyboardState;

    public static void Update()
    {
        previousMouseState = currentMouseState;
        currentMouseState = Mouse.GetState();

        previousKeyboardState = currentKeyboardState;
        currentKeyboardState = Keyboard.GetState();
    }

    public static Rectangle GetMouseBounds(bool currentState)
    {
        if (currentState)
            return new Rectangle(currentMouseState.X, currentMouseState.Y, 1, 1);
        else
            return new Rectangle(previousMouseState.X, previousMouseState.Y, 1, 1);
    }

    public static bool GetIsMouseButtonUp(MouseButton btn, bool currentState)
    {
        if (currentState)
            switch (btn)
            {
                case MouseButton.Left:
                    return currentMouseState.LeftButton == ButtonState.Released;
                case MouseButton.Middle:
                    return currentMouseState.MiddleButton == ButtonState.Released;
                case MouseButton.Right:
                    return currentMouseState.RightButton == ButtonState.Released;
            }
        else
            switch (btn)
            {
                case MouseButton.Left:
                    return previousMouseState.LeftButton == ButtonState.Released;
                case MouseButton.Middle:
                    return previousMouseState.MiddleButton == ButtonState.Released;
                case MouseButton.Right:
                    return previousMouseState.RightButton == ButtonState.Released;
            }

        return false;
    }

    public static bool GetIsMouseButtonDown(MouseButton btn, bool currentState)
    {
        return !GetIsMouseButtonUp(btn, currentState);
    }

    // TODO: Keyboard input stuff goes here.
}

public enum MouseButton
{
    Left,
    Middle,
    Right
}