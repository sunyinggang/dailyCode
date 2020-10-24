package com.syg.yiqing.service;

import com.syg.yiqing.dao.TraditionalOfficeDao;
import com.syg.yiqing.entity.FutureRoom;
import com.syg.yiqing.entity.TraditionalOffice;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.PageRequest;
import org.springframework.data.domain.Pageable;
import org.springframework.stereotype.Service;

import java.util.Date;
import java.util.List;

@Service
public class TraditionalOfficeService {

    @Autowired
    private TraditionalOfficeDao traditionalOfficeDao;

    public Page<TraditionalOffice> findAll(PageRequest pageable){
        return traditionalOfficeDao.findAll(pageable);
    }

    public Page<TraditionalOffice> findAllByCity(PageRequest pageable,String city){
        return traditionalOfficeDao.findAllByCity(pageable,city);
    }

    public Page<TraditionalOffice> findListLimitTime(PageRequest pageable, String city, String openTime){
        Page<TraditionalOffice> list = null;
        if(city != null){
            if(openTime != null){
                list = traditionalOfficeDao.findListLimitCityAndTime(pageable, city, openTime);
            }else{
                list = traditionalOfficeDao.findAllByCity(pageable, city);
            }
        }else{
            if(openTime != null){
                list = traditionalOfficeDao.findListLimitTime(pageable, openTime);
            }
        }
        return list;
    }
}
