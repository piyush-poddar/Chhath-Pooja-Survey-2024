jQuery(function(_0xb44ax1) {
    'use strict';
    _0xb44ax1('form#wrapped')['attr']('action', '/addrec');
    _0xb44ax1('#wizard_container')['wizard']({
        stepsWrapper: '#wrapped',
        submit: '.submit',
        beforeSelect: function(_0xb44ax4, _0xb44ax5) {
            if (_0xb44ax1('input#website')['val']()['length'] != 0) {
                return false
            };
            if (!_0xb44ax5['isMovingForward']) {
                return true
            };
            var _0xb44ax6 = _0xb44ax1(this)['wizard']('state')['step']['find'](':input');
            return !_0xb44ax6['length'] || !!_0xb44ax6['valid']()
        }
    })['validate']({
        errorPlacement: function(_0xb44ax2, _0xb44ax3) {
            if (_0xb44ax3['is'](':radio') || _0xb44ax3['is'](':checkbox')) {
                _0xb44ax2['insertBefore'](_0xb44ax3['next']())
            } else {
                _0xb44ax2['insertAfter'](_0xb44ax3)
            }
        }
    });
    _0xb44ax1('#progressbar')['progressbar']();
    _0xb44ax1('#wizard_container')['wizard']({
        afterSelect: function(_0xb44ax4, _0xb44ax5) {
            _0xb44ax1('#progressbar')['progressbar']('value', _0xb44ax5['percentComplete']);
            _0xb44ax1('#location')['text']('(' + _0xb44ax5['stepsComplete'] + '/' + _0xb44ax5['stepsPossible'] + ')')
        }
    });
    _0xb44ax1('#wrapped')['validate']({
        ignore: [],
        rules: {
            select: {
                required: true
            }
        },
        errorPlacement: function(_0xb44ax2, _0xb44ax3) {
            if (_0xb44ax3['is']('select:hidden')) {
                _0xb44ax2['insertAfter'](_0xb44ax3['next']('.nice-select'))
            } else {
                _0xb44ax2['insertAfter'](_0xb44ax3)
            }
        }
    })
});

function getVals(_0xb44ax8, _0xb44ax9) {
    switch (_0xb44ax9) {
        case 'question_1':
            var _0xb44axa = $(_0xb44ax8)['val']();
            $('#question_1')['text'](_0xb44axa);
            break;
        case 'question_2':
            var _0xb44axb = $(_0xb44ax8)['attr']('name');
            var _0xb44axa = [];
            $('input[name*=\'' + _0xb44axb + '\']')['each'](function() {
                if (jQuery(this)['is'](':checked')) {
                    _0xb44axa['push']($(this)['val']())
                }
            });
            $('#question_2')['text'](_0xb44axa['join'](', '));
            break;
        case 'question_3':
            var _0xb44axa = $(_0xb44ax8)['val']();
            $('#question_3')['text'](_0xb44axa);
            break;
        case 'additional_message':
            var _0xb44axa = $(_0xb44ax8)['val']();
            $('#additional_message')['text'](_0xb44axa);
            break
        case 'question_4':
            var _0xb44axa = $(_0xb44ax8)['val']();
            $('#question_4')['text'](_0xb44axa);
            break;
        case 'question_5':
            var _0xb44axa = $(_0xb44ax8)['val']();
            $('#question_5')['text'](_0xb44axa);
            break;
        case 'question_6':
            var _0xb44axa = $(_0xb44ax8)['val']();
            $('#question_6')['text'](_0xb44axa);
            break;
        case 'question_7':
            var _0xb44axa = $(_0xb44ax8)['val']();
            $('#question_7')['text'](_0xb44axa);
            break;
        case 'question_8':
            var _0xb44axa = $(_0xb44ax8)['val']();
            $('#question_8')['text'](_0xb44axa);
            break;
        case 'question_9':
            var _0xb44axa = $(_0xb44ax8)['val']();
            $('#question_9')['text'](_0xb44axa);
            break;
        case 'question_10':
            var _0xb44axa = $(_0xb44ax8)['val']();
            $('#question_10')['text'](_0xb44axa);
            break;
    }
}