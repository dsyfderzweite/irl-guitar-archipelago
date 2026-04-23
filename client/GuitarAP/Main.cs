using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Graphics;
using Microsoft.Xna.Framework.Input;
using GuitarAP.Code;
using System;

namespace GuitarAP;

public class Main : Game
{
    private GraphicsDeviceManager _graphics;
    private SpriteBatch _spriteBatch;
    public Vector2 ScreenSize { get; private set; }
    public static NotificationBox NotifBox;
    // private int _testCounter = 0;
    // private Button _testButton;
    private IGameScreen _activeScreen;

    public Main()
    {
        _graphics = new GraphicsDeviceManager(this);
        Content.RootDirectory = "Content";
        IsMouseVisible = true;
        ScreenSize = new(_graphics.PreferredBackBufferWidth, _graphics.PreferredBackBufferHeight);
        _activeScreen = new TitleScreen(this);
    }

    protected override void Initialize()
    {
        NotifBox = new NotificationBox(); // Would need to be re-initialized if the screen size changes, but that is not currently possible
        _activeScreen.Initialize();

        base.Initialize();
    }

    protected override void LoadContent()
    {
        _spriteBatch = new SpriteBatch(GraphicsDevice);
        NotifBox.LoadContent(Content, ScreenSize);
        _activeScreen.LoadContent(Content);
    }

    protected override void Update(GameTime gameTime)
    {
        InputManager.Update();
        NotifBox.Update(gameTime);
        _activeScreen.Update(gameTime);

        base.Update(gameTime);
    }

    protected override void Draw(GameTime gameTime)
    {
        GraphicsDevice.Clear(Color.AntiqueWhite);
        _spriteBatch.Begin();
        _activeScreen.Draw(_spriteBatch);
        NotifBox.Draw(_spriteBatch);
        _spriteBatch.End();

        base.Draw(gameTime);
    }
}
