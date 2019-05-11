# ski-weather-project

Програма обиратиме оптимальне місце у певній локації для лещетарства на основі погодних умов.

Вхідні дані: держава, дата  
Вихідні дані: рекомендації (локація - оптимальна/неоптимальна погода)
             
Коротка інструкція по користуванню  
Користувач вводить локацію(державу), де буде здійснюватися пошук гірськолижних курортів, і час. В результаті отримує інформацію з рекомендаціями місць, де найкраще (з боку погодних умов) займатись лижним спортом у певний період часу.

Структура програми  
Програма працює на основі даних отриманих за допомогою ключа SKI WEATHER API. Завдяки функції get_all_data() отримуються дані з погодними умовами у певній локації і записуються у файл. Функція convert_in() перетворює ці дані у абстрактний тип даних SkiWeather і зберігає їх у структурі даних Array. Функція main() "збирає все до купи" та виводить результат програми.

 
