package com.syg.yiqing.dao;

import com.syg.yiqing.entity.TraditionalOffice;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.jpa.repository.JpaRepository;

public interface TraditionalOfficeDao extends JpaRepository<TraditionalOffice, Integer> {

    @Override
    Page<TraditionalOffice> findAll(Pageable pageable);

    Page<TraditionalOffice> findAllByCity(Pageable pageable,String city);

}
