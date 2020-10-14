package com.syg.yiqing.service;

import com.syg.yiqing.dao.TraditionalOfficeDao;
import com.syg.yiqing.entity.TraditionalOffice;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.PageRequest;
import org.springframework.data.domain.Pageable;
import org.springframework.stereotype.Service;

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
}
