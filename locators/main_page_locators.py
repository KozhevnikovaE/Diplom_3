from selenium.webdriver.common.by import By


class MainPageLocators:
    # Кнопки навигации
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
    ORDER_FEED_BUTTON = (By.XPATH, "//a[@href='/feed']")

    # Ингредиенты и модальное окно
    INGREDIENT = (By.XPATH, "//a[contains(@class, 'BurgerIngredient')]")
    INGREDIENT_MODAL = (By.XPATH, "//div[contains(@class, 'Modal')]")
    CLOSE_MODAL_BUTTON = (By.XPATH, "//button[@type='button' and contains(@class, 'Modal_modal')]")

    # Счётчик ингредиента (первый в списке)
    COUNTER = (By.XPATH, "(//a[contains(@class, 'BurgerIngredient')])[1]//p[contains(@class, 'counter')]")

    # активное окно ленты заказов
    ORDER_FEED_ACTIVE = (By.XPATH, "//a[contains(@class, 'active')]//p[text()='Лента заказов']")

    # Поле для сборки бургера (цель для перетаскивания)
    CONSTRUCTOR_FIELD = (By.XPATH, "//section[contains(@class, 'BurgerConstructor')]")

    
    # счётчик (Выполнено за всё время)
    ORDER_FEED_ALL_TIME_COUNTER = (By.XPATH, "(//p[contains(@class, 'OrderFeed_number')])[1]")

    # счётчик (Выполнено за сегодня)
    ORDER_FEED_TODAY_COUNTER = (By.XPATH, "(//p[contains(@class, 'OrderFeed_number')])[2]")
 