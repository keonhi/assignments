# -*- coding: utf-8 -*-

def is369(n):
    '''어떤 수가 3이거나 6이거나 9인지 확인하는 함수'''
    return n in (3, 6, 9)

def count369(n):
    '''어떤 수에 있는 3,6,9의 개수 세는 함수'''
    if isinstance(n, int):
        if n > 0:
            if n<10: return int(is369(n))
            return is369(n%10)+count369(n//10)
        else:
            raise ValueError('0 이하의 정수는 사용할 수 없습니다.')
    else:
        raise TypeError('정수 이외의 자료형은 사용할 수 없습니다.')

def count369_except(n):
    '''양의 정수를 받아 count369() 함수를 실행하는 함수
    정수 이외의 자료형이 들어온 경우 TypeError를 반환하고
    0 이하의 정수가 들어온 경우 ValueError를 반환한다.'''
    try:
        return count369(n)
    except TypeError:
        print('이 자료형은 369 게임에서 사용할 수 없음:', type(n))
    except ValueError:
        print('이 값은 369 게임에 나오지 않음:', n)