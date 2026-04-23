using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Graphics;
using Microsoft.Xna.Framework.Content;
using System;

namespace GuitarAP.Code
{
    public class Button
    {
        public string Label { get; set; }
        public Action<GameTime> OnClick { get; set; }
        public ButtonStatus Status { get; private set; }
        public Rectangle Bounds { get; set; }
        private Color _buttonColor;
        private Texture2D _buttonTexture;
        private SpriteFont _labelFont;

        public Button(string label, Action<GameTime> onClick, Rectangle bounds)
        {
            Label = label;
            OnClick = onClick;
            Bounds = bounds;
            Status = ButtonStatus.Normal;
            _buttonColor = Color.LightGray;
        }

        public void LoadContent(ContentManager content)
        {
            _labelFont = content.Load<SpriteFont>("GenericFont");
            _buttonTexture = content.Load<Texture2D>("ButtonBackground");
        }

        public void Update(GameTime gameTime)
        {
            // If the mouse cursor is on our Button...
            if (InputManager.GetMouseBounds(true).Intersects(Bounds))
            {
                // And if the Left mouse button is down...
                if (InputManager.GetIsMouseButtonDown(MouseButton.Left, true))
                {
                    // Then our Button is down!
                    if (Status != ButtonStatus.Pressed)
                    {
                        // If the button was not already in the pressed state, we can trigger a click event immediately.
                        OnClick?.Invoke(gameTime);
                    }
                    Status = ButtonStatus.Pressed;
                }
                // Otherwise...
                else
                {
                    // The mouse cursor is simply hovering above our Button!
                    Status = ButtonStatus.Hovered;
                }
            }
            else
            {
                // If the cursor does not intersect with the Button then just set the state to normal.
                Status = ButtonStatus.Normal;
            }
        }

        public void Draw(SpriteBatch spriteBatch)
        {
            if (Status == ButtonStatus.Hovered)
                _buttonColor = Color.Gray;
            else if (Status == ButtonStatus.Pressed)
                _buttonColor = Color.DarkGray;
            else
                _buttonColor = Color.LightGray;
            spriteBatch.Draw(_buttonTexture, Bounds, _buttonColor);
            spriteBatch.DrawString(_labelFont, Label, new Vector2(Bounds.X + 10, Bounds.Y + 10), Color.Black);
        }
    }

    public enum ButtonStatus
    {
        // Button status is solely for graphical distinction and does not affect the button's functionality
        Normal,
        Hovered,
        Pressed
    }
}