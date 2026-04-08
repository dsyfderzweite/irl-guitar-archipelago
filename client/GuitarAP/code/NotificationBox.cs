using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Graphics;
using System.Collections.Generic;
using System;

namespace GuitarAP.Code
{
    public class NotificationBox
    {
        public List<(string message, TimeSpan addedTime)> Messages { get; set; }
        public List<String> MessageBuffer { get; set; }
        public int MaxMessages { get; set; } = 5;
        private SpriteFont _genericFont;
        private Vector2 _anchor; // The position of the bottom left corner of the screen
        public int _lifetime { get; set; } = 5; // in seconds

        public NotificationBox()
        {
            Messages = new List<(string, TimeSpan)>();
            // Maybe add a possibility for messages to be pre-loaded
            MessageBuffer = new List<string>();
        }

        public void AddMessage(string message, GameTime gameTime)
        {
            Messages.Insert(0, (message, gameTime.TotalGameTime));
            if (Messages.Count > MaxMessages)
            {
                Messages.RemoveAt(Messages.Count - 1);
            }
        }

        public void LoadContent(Microsoft.Xna.Framework.Content.ContentManager content, Vector2 screenSize)
        {
            _genericFont = content.Load<SpriteFont>("GenericFont");
            _anchor = new Vector2(_genericFont.LineSpacing, screenSize.Y);
        }

        public void Update(GameTime gameTime)
        {
            // Move buffered messages to active messages
            foreach (var msg in MessageBuffer)
            {
                AddMessage(msg, gameTime);
            }
            MessageBuffer.Clear();
            // Remove expired messages
            Messages.RemoveAll(m => (gameTime.TotalGameTime - m.addedTime).TotalSeconds > _lifetime);
        }

        public void Draw(GameTime gameTime, SpriteBatch spriteBatch)
        {
            for (int i = 0; i < Messages.Count; i++)
            {
                var msg = Messages[i];
                var position = _anchor - new Vector2(0, (i + 1) * (_genericFont.LineSpacing));
                spriteBatch.DrawString(_genericFont, msg.message, position, Color.Black);
            }
        }
    }
}