package com.robutpit.b2bplatform;

import android.graphics.Color;
import android.os.Bundle;
import android.webkit.WebView;
import com.getcapacitor.BridgeActivity;

public class MainActivity extends BridgeActivity {
    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        // Тёмная строка состояния в цвет сайта — без этого системная шторка
        // остаётся белой по умолчанию и выглядит как случайная деталь браузера,
        // а не часть приложения.
        getWindow().setStatusBarColor(Color.parseColor("#0F172A"));
    }

    @Override
    public void onBackPressed() {
        // Без этого аппаратная кнопка «назад» на Android закрывает всё
        // приложение с любой страницы — ощущается как краш, а не навигация.
        // Сначала листаем историю WebView (как в браузере), и только если
        // истории больше нет — сворачиваем/закрываем как обычно.
        WebView webView = getBridge().getWebView();
        if (webView != null && webView.canGoBack()) {
            webView.goBack();
        } else {
            super.onBackPressed();
        }
    }
}
