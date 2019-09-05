<?php

namespace frontend\controllers;

use yii\web\controllers;

class TestController extends \yii\web\Controller
{
    public function actionTest() {
        $dara = 'testxxxxxxxxxxx';
        return $this->render('index',[
            'xdata' => $dara
        ]);
    }
    
    
}
