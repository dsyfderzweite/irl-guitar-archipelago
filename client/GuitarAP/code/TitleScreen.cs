using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Graphics;
using Microsoft.Xna.Framework.Content;
using System.Net.Mail;

namespace GuitarAP.Code;

public class TitleScreen : IGameScreen
{
    private Game _game;
    private SpriteFont _titleFont;
    private Button _startButton, _settingsButton, _exitButton;


    public TitleScreen(Game game)
    {
        _game = game;
    }

    public void Initialize()
    {
        _startButton = new Button("Start Game",
                                  (gameTime) => Main.NotifBox.AddMessage("Start button clicked!", gameTime),
                                  new Rectangle(300, 200, 200, 50));
        _settingsButton = new Button("Settings",
                                     (gameTime) => Main.NotifBox.AddMessage("Settings button clicked!", gameTime),
                                     new Rectangle(300, 260, 200, 50));
        _exitButton = new Button("Exit",
                                  (gameTime) => _game.Exit(),
                                  new Rectangle(300, 320, 200, 50));
    }

    public void LoadContent(ContentManager content)
    {
        _titleFont = content.Load<SpriteFont>("GenericFont");
        _startButton.LoadContent(content);
        _settingsButton.LoadContent(content);
        _exitButton.LoadContent(content);
    }

    public void Update(GameTime gameTime)
    {
        _startButton.Update(gameTime);
        _settingsButton.Update(gameTime);
        _exitButton.Update(gameTime);
    }

    public void Draw(SpriteBatch spriteBatch)
    {
        spriteBatch.DrawString(_titleFont, "Guitar Archipelago", new Vector2(250, 100), Color.Black);
        _startButton.Draw(spriteBatch);
        _settingsButton.Draw(spriteBatch);
        _exitButton.Draw(spriteBatch);
    }
}